# Random-Articles-Generator

schema
{
    DOI,
    Pub_date,
    Title,
    
    Journal,
    Publisher,

    Authors: array
    Refs: array
    tags: array
    Doc:{
        Chapter:{
            Paragraphs: array di elements(textwall o url a img)
        }
    }
}
