/* This is from Code Institute Walkthrough project "I think therefor I blog" */    
document.addEventListener("DOMContentLoaded", function() {
  const editButtons = document.getElementsByClassName("btn-edit");
  const commentText = document.getElementById("id_body");
  const commentForm = document.getElementById("commentForm");

  const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
  const deleteButtons = document.getElementsByClassName("btn-delete");
  const deleteConfirm = document.getElementById("deleteConfirm");

  const deletePostModal = new bootstrap.Modal(document.getElementById("deletePostModal"));
  const deletePostButtons = document.getElementsByClassName("btn-delete-post");
  const deletePostConfirm = document.getElementById("deletePostConfirm");

  const editPostButtons = document.getElementsByClassName("btn-edit-post");
  const discussionPostForm = document.getElementById("discussionPostForm");

  const deleteCommentModal = new bootstrap.Modal(document.getElementById("deleteCommentModal"));
  const deleteDiscussionCommentModal = new bootstrap.Modal(document.getElementById("deleteDiscussionCommentModal"));
  const deleteCommentButtons = document.getElementsByClassName("btn-delete-comment");
  const deleteDiscussionCommentButtons = document.getElementsByClassName("btn-delete-discussion-comment");
  const deleteCommentConfirm = document.getElementById("deleteCommentConfirm");
  const deleteCommentConfirmDiscussion = document.getElementById("deleteCommentConfirmDiscussion");

  /**
  * Initializes edit functionality for the provided edit buttons.
  * 
  * For each button in the `editButtons` collection:
  * - Retrieves the associated comment's ID upon click.
  * - Fetches the content of the corresponding comment.
  * - Populates the `commentText` input/textarea with the comment's content for editing.
  * - Updates the submit button's text to "Update".
  * - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
  */
  for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      console.log("Edit button clicked")
      let commentId = e.target.getAttribute("comment_id");
      let commentContent = document.getElementById(`comment${commentId}`).innerText;
      commentText.value = commentContent;
      commentForm.setAttribute("action", `edit_comment/${commentId}`);
    });
  }
  /**
  * Initializes deletion functionality for the provided delete buttons.
  * 
  * For each button in the `deleteButtons` collection:
  * - Retrieves the associated comment's ID upon click.
  * - Updates the `deleteConfirm` link's href to point to the 
  * deletion endpoint for the specific comment.
  * - Displays a confirmation modal (`deleteModal`) to prompt 
  * the user for confirmation before deletion.
  */
 
  for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        deleteConfirm.href = `delete_comment/${commentId}`;
        deleteModal.show();
    });
  }
  
  /**
  * Initializes deletion functionality for the provided delete buttons in discussions.
  **/

  for (let button of deletePostButtons) {
    button.addEventListener("click", (e) => {
        let discussionPk = e.target.getAttribute("discussion_pk");
        deletePostConfirm.href = `/discussion/${discussionPk}/delete/`;
        deletePostModal.show();
    });
  }

    /**
  * Initializes edit functionality for the provided delete buttons in discussions.
  **/

  for (let button of editPostButtons) {
    button.addEventListener("click", (e) => {
      console.log("Edit button clicked");
      let discussionPk = e.target.getAttribute("discussion_pk");
      let discussionContent = document.getElementById(`discussion${discussionPk}`).innerText;
      discussionText.value = discussionContent;
      discussionPostForm.setAttribute("action", `edit_post/${discussionPk}`);
    });
  }

    /**
  * Initializes deletion functionality for the provided delete buttons in blog comments.
  **/

  for (let button of deleteCommentButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("comment_id");
      let postSlug = e.target.getAttribute("post_slug");
      deleteCommentConfirm.href = `/post/${postSlug}/delete_comment/${commentId}/`;
      deleteCommentModal.show();
    });
  }

    /**
  * Initializes deletion functionality for the provided delete buttons in discussion comments.
  **/

  for (let button of deleteDiscussionCommentButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("comment_id");
      let discussionID = e.target.getAttribute("discussion_id");
      deleteCommentConfirmDiscussion.href = `/discussion/post/${discussionID}/delete_comment/${commentId}/`;
      deleteDiscussionCommentModal.show();
    });
  }
  

});
