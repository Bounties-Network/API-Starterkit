const express = require('express');
const validate = require('express-validation');
const paramValidation = require('../../config/param-validation');
const authCtrl = require('./auth.controller');

const router = express.Router(); // eslint-disable-line new-cap

/** POST /api/auth/login - Returns token if correct username and password is provided */
router.route('/login')
  .post(validate(paramValidation.login), authCtrl.login);

router.route('/logout')
  .get(authCtrl.logout);

/** GET /api/auth/random-number - Protected route,
 * needs token returned by the above as header. Authorization: Bearer {token} */
router.route('/:public_address/nonce')
  .get(validate(paramValidation.nonce), authCtrl.nonce);

router.route('/user')
  .get(authCtrl.currentUser);

module.exports = router;
