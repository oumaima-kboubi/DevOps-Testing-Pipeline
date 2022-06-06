describe("Let's add a new task",()=> {
 it("Visit TODO List Demo App",()=>{
    cy.visit(" http://127.0.0.1:5000/tasks/home");
    cy.get('[style="text-align: right;"] > .btn').click();
    cy.get('#newTask').should('be.visible');
    cy.get('#newTask').type('Pla guitar');
    // cy.get('#closeModal').should('be.non.visible');
     cy.get('#submit-task').click();
    });
});


 
describe("Let's delete some tasks",()=> {
    it("Visit TODO List Demo App",()=>{
       cy.visit(" http://127.0.0.1:5000/tasks/home");
       
       cy.get(':nth-child(7) > :nth-child(5) > .btn').click();
       
       });
   });
