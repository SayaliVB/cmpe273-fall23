Based on the lab 1, implement GraphQL endpoint to serve these operations using StrawberryLinks to an external site.:

Create Item
Update Item
Delete Item
Query Item by id
Item Model:

type Query {

 item: Item

}

type Item {

 id: ID!

 name: String!

}