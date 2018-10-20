const Joi = require('joi');

module.exports = {
  updateUser: {
    body: {
      username: Joi.string().required(),
    },
    params: {
      public_address: Joi.string().required()
    }
  },
  login: {
    body: {
      public_address: Joi.string().required(),
      signature: Joi.string().required()
    }
  },
  nonce: {
    params: {
      public_address: Joi.string().required()
    }
  }
};
