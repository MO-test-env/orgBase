/**
 * Appends a message to an existing GitHub comment.
 * 
 * @param {import('@actions/github').GitHub} github - GitHub client
 * @param {number} commentId - ID of the comment to update
 * @param {string} message - Message to append
 * @param {string} owner - repo owner
 * @param {string} repo - repo name
 */
async function appendToComment(github, commentId, message, owner, repo) {
  // Get the current comment body
  const { data: comment } = await github.rest.issues.getComment({
    owner,
    repo,
    comment_id: commentId,
  });

  // Append the message
  const newBody = comment.body + "\n" + message;

  // Update the comment
  await github.rest.issues.updateComment({
    owner,
    repo,
    comment_id: commentId,
    body: newBody,
  });
}

module.exports = appendToComment;
