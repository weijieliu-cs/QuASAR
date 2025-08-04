# QuASAR
Question-driven, structure-aware self-supervised framework for table-to-text generation (ACL 2025)


### Notice on ToTTo Dataset and Code Updates

The current implementation used for processing the ToTTo dataset was originally developed during the ACL 2025 submission phase. Due to the presence of many irregular tables in ToTTo, our initial code includes some rough and ad-hoc handling strategies. Despite these limitations, the experimental results reported in the paper are fully reproducible.

To make the codebase cleaner and easier to understand, we are now working on cleaning the ToTTo dataset by filtering or fixing malformed tables. This will allow us to streamline the data processing pipeline and improve the clarity of the implementation.

As we are currently preparing a submission for ICLR 2026, our available time is limited. Therefore, we plan to gradually release the full QuASAR codebase and the cleaned version of the ToTTo dataset in stages. We appreciate your patience and understanding.