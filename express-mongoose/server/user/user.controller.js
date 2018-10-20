const httpStatus = require('http-status');
const APIError = require('../helpers/APIError');

/**
 * Update existing user
 * @property {string} req.body.username - The username of user.
 * @property {string} req.body.mobileNumber - The mobileNumber of user.
 * @returns {User}
 */
function update(req, res, next) {
  const user = req.user;
  if (!user || user.public_address !== req.params.public_address.toLowerCase()) {
    const err = new APIError('Authentication error', httpStatus.UNAUTHORIZED, true);
    return next(err);
  }

  user.username = req.body.username;
  user.save()
    .then(savedUser => res.json(savedUser))
    .catch(e => next(e));
}

module.exports = { update };
