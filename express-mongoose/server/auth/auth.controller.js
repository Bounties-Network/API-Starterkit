const httpStatus = require('http-status');
const APIError = require('../helpers/APIError');
const User = require('../user/user.model');
const uuidv4 = require('uuid/v4');
const Web3 = require('web3');

const web3 = new Web3(Web3.givenProvider);

function nonce(req, res, next) {
  const publicAddress = req.params.public_address.toLowerCase();
  User.get(publicAddress)
    .then((user) => {
      const userNonce = uuidv4();
      if (!user.length) {
        const newUser = new User({
          public_address: publicAddress,
          nonce: userNonce,
        });

        newUser.save()
          .then(() => res.json({ nonce: userNonce }))
          .catch(e => next(e));
      }
      return res.json({ nonce: user[0].nonce });
    })
    .catch(e => next(e));
}

function login(req, res, next) {
  const publicAddress = req.body.public_address.toLowerCase();
  const signature = req.body.signature;
  const err = new APIError('Authentication error', httpStatus.UNAUTHORIZED, true);
  User.get(publicAddress)
    .then((users) => {
      if (!users.length) {
        next(err);
      }
      const user = users[0];
      const calculatedPublicAddress = web3.eth.accounts.recover(`Hi there! Your special nonce: ${user.nonce}`, signature);
      user.nonce = uuidv4();
      user.save()
        .then((savedUser) => {
          if (calculatedPublicAddress.toLowerCase() === publicAddress) {
            req.session.currentUser = savedUser.public_address;
            return res.json(savedUser);
          }
          return next(err);
        })
        .catch(e => next(e));
    })
    .catch(e => next(e));
}

function logout(req, res) {
  req.session.destroy();
  return res.send('success');
}

function currentUser(req, res, next) {
  if (req.user) {
    return res.json(req.user);
  }
  const err = new APIError('Authentication error', httpStatus.UNAUTHORIZED, true);
  next(err);
}

module.exports = { login, logout, nonce, currentUser };
