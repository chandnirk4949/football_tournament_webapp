// scripts for the web app

// logout confirmation dialog
function confirmLogout() {
  var confirmation = confirm("Are you sure you want to log out?");
  if (confirmation) {
    // Logout
    window.location.href = "/";
  }
}


// to dynamically add members to the team registration page
const addMemberButton = document.getElementById('add-member-button');
const submitButton = document.getElementById('submit-button');
let memberCount = 1;
const maxMemberCount = 21;

document.getElementById("add-member-button").addEventListener("click", function () {
  // Check if the maximum number of members has been reached
  if (memberCount >= maxMemberCount) {
    return;
  }

  // Create a new row element for the member details
  const memberRow = document.createElement("div");
  memberRow.classList.add("member-row");

  // Create a new member name label
  const memberNameLabel = document.createElement('label');
  memberNameLabel.for = 'member_name';
  memberNameLabel.textContent = 'Member Name';
  memberRow.appendChild(memberNameLabel);

  // Create an input element for the member name
  const memberNameInput = document.createElement("input");
  memberNameInput.type = "text";
  memberNameInput.name = "member_name";
  memberNameInput.required = true;
  memberRow.appendChild(memberNameInput);

  // Create a new role label
  const roleLabel = document.createElement('label');
  roleLabel.for = 'role';
  roleLabel.textContent = 'Role';
  memberRow.appendChild(roleLabel);

  // Create a select element for the member role
  const memberRoleSelect = document.createElement("select");
  memberRoleSelect.name = "member_role";
  memberRoleSelect.innerHTML = `
    <option value="player">Player</option>
    <option value="coach">Coach</option>
    <option value="manager">Manager</option>
  `;
  memberRow.appendChild(memberRoleSelect);

  // Create a button to remove the member row
  const removeMemberButton = document.createElement("button");
  removeMemberButton.type = "button";
  removeMemberButton.classList.add("remove-member-button");
  removeMemberButton.textContent = "Remove member";
  memberRow.appendChild(removeMemberButton);

  // Append the member row to the member list
  document.getElementById("member-list").appendChild(memberRow);

  // Increment the member count
  memberCount++;

  // Add an event listener to the remove member button
  removeMemberButton.addEventListener("click", function () {
    // Remove the member row from the member list
    memberRow.parentNode.removeChild(memberRow);

    // Decrement the member count
    memberCount--;
    if (memberCount < maxMemberCount) {
      console.log("Member count");
      document.getElementById('add-member-button').disabled = false;
    }
  });

  // Disable the add member button if the maximum number of members has been reached
  if (memberCount >= maxMemberCount) {
    addMemberButton.disabled = true;
  }
});


// Use jQuery to handle the click eevent on the view member button on teams data page
$(document).ready(function () {
  $('.view-members-button').click(function () {
    console.log("Member count")
    var teamId = $(this).data('team-id');

    // Make an AJAX request to fetch team members
    $.get('/team_members/' + teamId + '/', function (data) {
      // Populate the team members list
      var membersList = document.getElementById('teamMembersList');
      membersList.innerHTML = '';

      for (var i = 0; i < data.members.length; i++) {
        var member = data.members[i];
        var listItem = document.createElement('li');
        listItem.innerHTML = '<strong>Name:</strong> ' + member.name + ', <strong>Role:</strong> ' + member.role;
        membersList.appendChild(listItem);
      }

      // Show the modal
      $('#teamMembersModal').modal('show');
    });
  });
});




