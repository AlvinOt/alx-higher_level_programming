#!/usr/bin/node
exports.callMeMoby = function (x, theFunct) {
  for (let i = 0; i < x; i++) theFunct();
};
