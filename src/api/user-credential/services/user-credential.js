'use strict';

/**
 * user-credential service.
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::user-credential.user-credential');
